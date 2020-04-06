from . import consumers
from channels.routing import ProtocolTypeRouter

channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
}


application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
