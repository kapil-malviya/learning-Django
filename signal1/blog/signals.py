from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created    # signal for initial connection to the database


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('\n\n--------------------\n\n Logged in Signal... Run Intro...')
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('user password :', user.password)
    print(f'kwargs : {kwargs}')

# another way of connecting to the signal or use decorator
# user_logged_in.connect(login_success, sender=User)
    

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print('\n\n--------------------\n\n Logged Out Signal... Run Outro...')
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('user password :', user.password)
    print(f'kwargs : {kwargs}')
# another way of connecting to the signal or use decorator
# user_logged_out.connect(logout_success, sender=User)


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('\n\n--------------------\n\n Logged In Failed ... Run Intro...')
    print('sender : ', sender)
    print('request : ', request)
    print('credentials : ', credentials)
    print(f'kwargs : {kwargs}')
# another way of connecting to the signal or use decorator
# user_login_failed.connect(login_failed)



@receiver(pre_save, sender=User)
def save_at_begining(sender, instance, **kwargs):
    print('\n\n--------------------\n\n Pre Save Signal ...')
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
# pre_save.connect(save_at_begining, sender=User)
    


@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if created:
        print('\n\n-------------------\n\n Post Save Signal ... \n')
        print('\n New Record ')
        print('Sender : ', sender)
        print('instance : ', instance)
        print('Created : ', created)
        print(f'kwargs : {kwargs}')
    else:
        print('\n\n--------------------\n\n  Post Save Signal .. ')
        print('\n Record Update')
        print('sender : ', sender)
        print('instance : ', instance)
        print('created : ', created)
        print(f'kwargs : {kwargs}')

# post_save.connect(post_save, sender=User)
        



@receiver(pre_delete, sender=User)
def at_begining_delete(sender, instance, **kwargs):
    print('\n\n-------------------\n\n Post Save Signal ... \n')
    print('--------- Pre Delete Signal ---------\n')
    print('Sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
# pre_delete.connect(at_begining_delete, sender=User)
    


@receiver(post_delete, sender=User)
def at_end_delete(sender, instance, **kwargs):
    print('\n\n\t--\t\n\n')
    print('--- Post Delete Signal ---')
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'kwargs : {kwargs}')
# post_delete.connect(at_end_delete, sender=User)
    




@receiver(pre_init, sender=User)
def at_begining_init(sender, *args, **kwargs):
    print('\n\n-------------------\n\n Post Save Signal ... \n')
    print('--------- Pre Init Signal ---------\n')
    print('Sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
# pre_init.connect(at_begining_init, sender=User)
    


@receiver(post_init, sender=User)
def at_end_init(sender, *args, **kwargs):
    print('\n\n\t--\t\n\n')
    print('--- Post Init Signal ---')
    print('sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
# post_init.connect(at_end_init, sender=User)
    


@receiver(request_started)
def at_begining_request(sender, environ, **kwargs):
    print('\n\n---\n\n')
    print('At begining Request')
    print('sender : ', sender)
    print('environ : ', environ)
    print(f'kwargs : {kwargs}')
# request_started.connect(at_begining_request)
    

@receiver(request_finished)
def at_end_request(sender, **kwargs):
    print('\n\n---\n\n')
    print('At end of Request')
    print('sender : ', sender)
    print(f'kwargs : {kwargs}')
# request_finished.connect(at_end_request)
    

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print('\n\n-------------\n\n')
    print('At Request Exception')
    print('sender : ', sender)
    print('request : ', request)
    print(f'kwargs : {kwargs}')
# got_request_exception.connect((at_request_exception))
    


@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print ('\n\n---\n\n')
    print('---- before_install_app ----')
    print('Sender : ', sender)
    print('App_config : ', app_config)
    print('Verbosity : ', verbosity)
    print('Interactive : ', interactive)
    print('Using : ', using)
    print('plan : ', plan)
    print('App : ', apps)
    print (f'Kwargs : {kwargs}')
# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('\n\n\t---\t\n\n')
    print('---\t at_end_migrate_flush \t---')
    print('sender : ', sender)
    print('App_config : ', app_config)
    print('verbosity : ', verbosity)
    print('Interactive : ', interactive)
    print('using : ', using)
    print('plan : ', plan)
    print('app : ', apps)
    print(f'kwargs : {kwargs}')
# post_migrate.connect(at_end_migrate_flush)
    



@receiver(connection_created)
def connect_db(sender, connection, **kwargs):
    print('\n\n\t --- \t\n\n')
    print('Initial Connection to the database')
    print('sender : ', sender)
    print('connection : ', connection)
    print(f'kwargs : {kwargs}')
# connection_created.connect(connect_db)
