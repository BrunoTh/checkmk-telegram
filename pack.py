import mkp

NAME = "checkmk-telegram"
VERSION = '1.0.0'

info = {
  'author': 'Bruno Thienel',
  'description': 'A notifcation plugin for telegram.',
  'download_url': 'https://github.com/BrunoTh/checkmk-telegram',
  'files': mkp.find_files(''),
  'name': 'checkmk-telegram',
  'title': 'Telegram Notifications',
  'version': VERSION,
  'version.min_required': '2.0.0',
}

mkp.pack_to_file(info, '', '%s-%s.mkp' % (NAME, VERSION))
