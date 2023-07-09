from winotify import Notification, audio


def notify_work():
    toast = Notification(app_id="PMODORO",
                                title="Now time to Focus!!!",
                                msg="Don't be distracted, complete your work for now!",
                                icon=r"C:\Users\Harshitha\PycharmProjects\Pomodoro\tomato.png")
    toast.set_audio(audio.Mail, loop=False)
    toast.show()


def notify_short():
    toast = Notification(app_id="PMODORO",
                         title="Now time to take a break!",
                         msg=" Time where you are free to do anything!",
                         icon=r"C:\Users\Harshitha\PycharmProjects\Pomodoro\tomato.png")
    toast.set_audio(audio.SMS, loop=False)
    toast.show()


def notify_long():
    toast = Notification(app_id="PMODORO",
                         title="Now time to take a long break!",
                         msg="Go for a walk!, drink water, jump around, relax you are doing great!!",
                         icon=r"C:\Users\Harshitha\PycharmProjects\Pomodoro\tomato.png")
    toast.set_audio(audio.LoopingCall, loop=True)
    toast.show()

def notify_one_session():
    toast = Notification(app_id="PMODORO",
                         title="One Pomodoro done!",
                         msg="click on start for another session",
                         icon=r"C:\Users\Harshitha\PycharmProjects\Pomodoro\tomato.png")
    toast.set_audio(audio.LoopingCall, loop=True)
    toast.show()


