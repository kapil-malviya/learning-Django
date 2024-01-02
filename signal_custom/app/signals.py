from django.dispatch import Signal, receiver

# creating signals

notification = Signal()


# receiver function

@receiver(notification)
def show_notification(sender, **kwargs):
	print('\n\n\t---\n\n')
	print('sender : ', sender)
	print(f'kwargs : {kwargs}')
	print('\n\t---\t Notification ---\n')


# we have made signal, now we have to send it (send in views)