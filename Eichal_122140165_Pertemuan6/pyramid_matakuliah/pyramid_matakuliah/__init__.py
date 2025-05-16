from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import get_session_factory, get_engine, Base

def main(global_config, **settings):
    # Buat engine database
    engine = get_engine(settings, prefix='sqlalchemy.')
    # Buat session factory
    session_factory = get_session_factory(engine)
    # Bind metadata (optional, tapi biasanya tidak wajib kalau sudah binding engine ke session factory)
    Base.metadata.bind = engine

    with Configurator(settings=settings) as config:
        # Simpan session factory di registry supaya bisa diakses dari views
        config.registry['dbsession_factory'] = session_factory
        
        # Tambahkan method request.dbsession supaya bisa dipakai di view secara otomatis
        config.add_request_method(
            lambda request: session_factory(),
            'dbsession',
            reify=True
        )

        # Tambahkan route home supaya tidak error "No route named home found"
        config.add_route('home', '/')

        # Tambahkan route lain
        config.add_route('list_matkul', '/matakuliah')
        config.add_route('get_matkul', '/matakuliah/{id}')
        config.add_route('create_matkul', '/matakuliah')
        config.add_route('update_matkul', '/matakuliah/{id}')
        config.add_route('delete_matkul', '/matakuliah/{id}')

        # Scan semua views yang terdaftar di package
        config.scan()

        # Return aplikasi WSGI
        return config.make_wsgi_app()
