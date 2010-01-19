import os
from django.conf import settings

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
###   original tinymce config
#        {'theme': "simple", 'relative_urls': False})

            {
                'plugins': 'advimage,advlink,table,searchreplace,contextmenu,template,paste,save,autosave',
            	'mode':'exact',
                'theme': 'advanced',
                'cleanup_on_startup': True,
                'custom_undo_redo_levels': 100,
            	#Theme options
            	'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontsizeselect",
            	'theme_advanced_buttons2' : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,forecolor",
            	'theme_advanced_buttons3' : "tablecontrols,|,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
            	'theme_advanced_toolbar_location' : "top",
            	'theme_advanced_toolbar_align' : "center",
            	'theme_advanced_statusbar_location' : "bottom",
                'width' : '90%',
                'height' : 480,

                'gecko_spellcheck' : True,
              	#Manifest common.css
            	'content_css': settings.STATIC_URL+'css/editor.css',
            }
        )

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

JS_URL = getattr(settings, 'TINYMCE_JS_URL',
###   original tinymce config
#        '%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL)

        '%stinymce/jscripts/tiny_mce/tiny_mce.js' % settings.MEDIA_URL)

JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT',
###   original tinymce config
#        os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

        os.path.join(settings.MEDIA_ROOT, 'tinymce/jscripts/tiny_mce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
