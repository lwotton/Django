user_registered.connect(create_profile)

def create_profile(sender, instance, request, **kwargs):
    from tracker.models import UserProfile
    #If you want to set any values (perhaps passed via request) 
    #you can do that here

    Profile(user = instance).save()