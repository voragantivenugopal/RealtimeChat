from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from .models import RealEditor
from .serializers import RealEditorSerializer


class NotificationRouter(ModelPubRouter):
    valid_verbs = ['subscribe']
    route_name = 'editors'
    model = RealEditor
    serializer_class = RealEditorSerializer


route_handler.register(NotificationRouter)
