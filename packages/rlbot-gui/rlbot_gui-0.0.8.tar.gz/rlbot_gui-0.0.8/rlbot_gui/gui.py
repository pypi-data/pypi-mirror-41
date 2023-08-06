import configparser
import os
import string
import tempfile
import urllib.request
import zipfile

import eel
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QFileDialog
from pip._internal import main as pipmain
from rlbot.agents.base_agent import BOT_CONFIG_MODULE_HEADER, BOT_NAME_KEY, PYTHON_FILE_KEY, BaseAgent
from rlbot.matchconfig.match_config import PlayerConfig, MatchConfig, MutatorConfig
from rlbot.parsing.bot_config_bundle import get_bot_config_bundle, BotConfigBundle
from rlbot.parsing.directory_scanner import scan_directory_for_bot_configs
from rlbot.parsing.incrementing_integer import IncrementingInteger
from rlbot.parsing.match_settings_config_parser import map_types, game_mode_types, \
    boost_amount_mutator_types, match_length_types, max_score_types, overtime_mutator_types, \
    series_length_mutator_types, game_speed_mutator_types, ball_max_speed_mutator_types, ball_type_mutator_types, \
    ball_weight_mutator_types, ball_size_mutator_types, ball_bounciness_mutator_types, rumble_mutator_types, \
    boost_strength_mutator_types, gravity_mutator_types, demolish_mutator_types, respawn_time_mutator_types
from rlbot.setup_manager import SetupManager

DEFAULT_BOT_FOLDER = 'default_bot_folder'

sm: SetupManager = None
settings = QSettings('rlbotgui', 'preferences')

def create_player_config(bot, human_index_tracker: IncrementingInteger):
    player_config = PlayerConfig()
    player_config.bot = bot['type'] in ('rlbot', 'psyonix')
    player_config.rlbot_controlled = bot['type'] in ('rlbot', 'party_member_bot')
    player_config.bot_skill = 1.0
    player_config.human_index = 0 if player_config.bot else human_index_tracker.increment()
    player_config.name = bot['name']
    player_config.team = int(bot['team'])
    if 'path' in bot and bot['path']:
        player_config.config_path = bot['path']
    return player_config


def start_match_helper(bot_list, match_settings):
    print(bot_list)
    print(match_settings)
    num_participants = len(bot_list)

    match_config = MatchConfig()
    match_config.num_players = num_participants
    match_config.game_mode = match_settings['game_mode']
    match_config.game_map = match_settings['map']
    match_config.mutators = MutatorConfig()

    mutators = match_settings['mutators']
    match_config.mutators.match_length = mutators['match_length']
    match_config.mutators.max_score = mutators['max_score']
    match_config.mutators.overtime = mutators['overtime']
    match_config.mutators.series_length = mutators['series_length']
    match_config.mutators.game_speed = mutators['game_speed']
    match_config.mutators.ball_max_speed = mutators['ball_max_speed']
    match_config.mutators.ball_type = mutators['ball_type']
    match_config.mutators.ball_weight = mutators['ball_weight']
    match_config.mutators.ball_size = mutators['ball_size']
    match_config.mutators.ball_bounciness = mutators['ball_bounciness']
    match_config.mutators.boost_amount = mutators['boost_amount']
    match_config.mutators.rumble = mutators['rumble']
    match_config.mutators.boost_strength = mutators['boost_strength']
    match_config.mutators.gravity = mutators['gravity']
    match_config.mutators.demolish = mutators['demolish']
    match_config.mutators.respawn_time = mutators['respawn_time']

    human_index_tracker = IncrementingInteger(0)
    match_config.player_configs = [create_player_config(bot, human_index_tracker) for bot in bot_list]

    global sm
    if sm is not None:
        try:
            sm.shut_down()
        except Exception as e:
            print(e)

    sm = SetupManager()
    sm.connect_to_game()
    sm.load_match_config(match_config)
    sm.launch_ball_prediction()
    sm.launch_quick_chat_manager()
    sm.launch_bot_processes()
    sm.start_match()
    # Note that we are not calling infinite_loop because that is not compatible with the way eel works!
    # Instead we will reproduce the important behavior from infinite_loop inside this file.


@eel.expose
def start_match(bot_list, match_settings):
    eel.spawn(start_match_helper, bot_list, match_settings)


@eel.expose
def kill_bots():
    if sm is not None:
        sm.shut_down(time_limit=5, kill_all_pids=True)
    else:
        print("There gotta be some setup manager already")


@eel.expose
def pick_bot_folder():
    filename = pick_bot_location(True)

    if filename:
        settings.setValue(DEFAULT_BOT_FOLDER, filename)
        settings.sync()
        return scan_for_bots(filename)

    return []


def load_bundle(filename):
    try:
        bundle = get_bot_config_bundle(filename)
        return [{
            'name': bundle.name,
            'type': 'rlbot',
            'image': 'imgs/rlbot.png',
            'path': bundle.config_path,
            'info': read_info(bundle)
        }]
    except Exception as e:
        print(e)

    return []


@eel.expose
def pick_bot_config():
    filename = pick_bot_location(False)
    return load_bundle(filename)


def pick_bot_location(is_folder):
    """
    We're using python for file picking because only python (not javascript) can retrieve
    an actual path on the file system which is what we need.
    https://stackoverflow.com/questions/2809688/directory-chooser-in-html-page

    :return:
    """

    app = QApplication([])
    options = QFileDialog.Options()

    if is_folder:
        filename = QFileDialog.getExistingDirectory(options=options)
    else:
        filename, _ = QFileDialog.getOpenFileName(filter="Config files (*.cfg)", options=options)

    app.exit()

    return filename


def read_info(bundle: BotConfigBundle):
    details_header = 'Details'
    if bundle.base_agent_config.has_section(details_header):
        return {
            'developer': bundle.base_agent_config.get(details_header, 'developer'),
            'description': bundle.base_agent_config.get(details_header, 'description'),
            'fun_fact': bundle.base_agent_config.get(details_header, 'fun_fact'),
            'github': bundle.base_agent_config.get(details_header, 'github'),
            'language': bundle.base_agent_config.get(details_header, 'language'),
        }
    return None


@eel.expose
def scan_for_bots(directory):
    bot_directory = directory or settings.value(DEFAULT_BOT_FOLDER, type=str) or "."
    return [
        {
            'name': bundle.name,
            'type': 'rlbot',
            'image': 'imgs/rlbot.png',
            'path': bundle.config_path,
            'info': read_info(bundle)
        }
        for bundle in scan_directory_for_bot_configs(bot_directory)]


@eel.expose
def get_language_support():
    java_return_code = os.system("java -version")
    # Only bother returning iffy languages. No point in sending 'python': True
    return {
        'java': java_return_code == 0,
        'chrome': is_chrome_installed(),  # Scratch bots need chrome to auto-run
    }


@eel.expose
def get_match_options():
    return {
        'map_types': map_types,
        'game_modes': game_mode_types,
        'mutators': {
            'match_length_types': match_length_types,
            'max_score_types': max_score_types,
            'overtime_types': overtime_mutator_types,
            'series_length_types': series_length_mutator_types,
            'game_speed_types': game_speed_mutator_types,
            'ball_max_speed_types': ball_max_speed_mutator_types,
            'ball_type_types': ball_type_mutator_types,
            'ball_weight_types': ball_weight_mutator_types,
            'ball_size_types': ball_size_mutator_types,
            'ball_bounciness_types': ball_bounciness_mutator_types,
            'boost_amount_types': boost_amount_mutator_types,
            'rumble_types': rumble_mutator_types,
            'boost_strength_types': boost_strength_mutator_types,
            'gravity_types': gravity_mutator_types,
            'demolish_types': demolish_mutator_types,
            'respawn_time_types': respawn_time_mutator_types
        }
    }


@eel.expose
def install_package(package_string):
    exit_code = pipmain(['install', package_string])
    print(exit_code)
    return {'exitCode': exit_code, 'package': package_string}


def download_and_extract_zip(download_url, local_zip_path, local_folder_path):
    urllib.request.urlretrieve(download_url, local_zip_path)

    with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
        zip_ref.extractall(local_folder_path)


@eel.expose
def download_bot_pack():
    # See https://docs.google.com/document/d/10uCWwHDQYJGMGeoaW1pZu1KvRnSgm064oWL2JVx4k4M/edit?usp=sharing
    # To learn how the bot pack file is hosted and maintained.
    download_and_extract_zip(
        download_url="https://drive.google.com/uc?export=download&id=1OOisnGpxD48x_oAOkBmzqNdkB5POQpiV",
        local_zip_path="RLBotPack.zip", local_folder_path=".")


@eel.expose
def show_bot_in_explorer(bot_cfg_path):
    import subprocess
    directory = os.path.dirname(bot_cfg_path)
    subprocess.Popen(f'explorer "{directory}"')


@eel.expose
def hot_reload_python_bots():
    if sm is not None:
        sm.reload_all_agents()


def convert_to_filename(text):
    """
    Normalizes string, converts to lowercase, removes non-alphanumeric characters,
    and converts spaces to underscores.
    """
    import unicodedata
    normalized = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in normalized if c in valid_chars)
    filename = filename.replace(' ', '_')  # Replace spaces with underscores
    return filename


@eel.expose
def begin_python_bot(bot_name):
    bot_directory = settings.value(DEFAULT_BOT_FOLDER, type=str) or "."
    sanitized_name = convert_to_filename(bot_name)

    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)

        download_and_extract_zip(
            download_url="https://github.com/RLBot/RLBotPythonExample/archive/master.zip",
            local_zip_path=f"{tmpdirname}/RLBotPythonExample.zip", local_folder_path=tmpdirname)

        try:
            os.rename(f"{tmpdirname}/RLBotPythonExample-master", f"{bot_directory}/{sanitized_name}")
        except FileExistsError:
            return {'error': f'There is already a bot named {sanitized_name}, please choose a different name!'}

    # Choose appropriate file names based on the bot name
    code_dir = f"{bot_directory}/{sanitized_name}/{sanitized_name}"
    python_file = f"{code_dir}/{sanitized_name}.py"
    config_file = f"{code_dir}/{sanitized_name}.cfg"

    # We're making some big assumptions here that the file structure / names in RLBotPythonExample will not change.
    os.rename(f"{bot_directory}/{sanitized_name}/python_example/", code_dir)
    os.rename(f"{code_dir}/python_example.py", python_file)
    os.rename(f"{code_dir}/python_example.cfg", config_file)

    # Update the config file to point to the renamed files, and show the correct bot name.
    raw_bot_config = configparser.RawConfigParser()
    raw_bot_config.read(config_file, encoding='utf8')
    agent_config = BaseAgent.base_create_agent_configurations()
    agent_config.parse_file(raw_bot_config)
    agent_config.set_value(BOT_CONFIG_MODULE_HEADER, BOT_NAME_KEY, bot_name)
    agent_config.set_value(BOT_CONFIG_MODULE_HEADER, PYTHON_FILE_KEY, f"{sanitized_name}.py")
    with open(config_file, "w", encoding='utf8') as f:
        f.write(str(agent_config))

    # This is intended to open the example python file in the default system editor for .py files.
    # Hopefully this will be VS Code or notepad++ or something. If it gets executed as a python script, no harm done.
    os.startfile(python_file)

    return {'bots': load_bundle(config_file)}


should_quit = False


def on_websocket_close(page, sockets):
    global should_quit
    eel.sleep(3.0)  # We might have just refreshed. Give the websocket a moment to reconnect.
    if not len(eel._websockets):
        # At this point we think the browser window has been closed.
        should_quit = True
        if sm is not None:
            sm.shut_down(time_limit=5, kill_all_pids=True)


def is_chrome_installed():
    return eel.browsers.chr.get_instance_path() is not None


def start():
    gui_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gui')
    eel.init(gui_folder)

    options = {}
    if not is_chrome_installed():
        options = {'mode': 'system-default'}  # Use the system default browser if the user doesn't have chrome.

    # This disable_cache thing only works if you have tare's fork of eel
    # https://github.com/tarehart/Eel/commit/98395ccc268e1a7a5137da2515b472fcc03db5c5
    # installed to pip locally using this technique https://stackoverflow.com/a/49684835
    eel.start('main.html', size=(1000, 800), block=False, callback=on_websocket_close, options=options,
              disable_cache=True)

    while not should_quit:
        if sm:
            sm.try_recieve_agent_metadata()
        eel.sleep(1.0)
