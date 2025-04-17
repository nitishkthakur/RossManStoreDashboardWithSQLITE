import callbacks_promo
import callbacks_performance



def register_callbacks(app):
    callbacks_promo.register_callbacks(app)
    callbacks_performance.register_callbacks(app)

