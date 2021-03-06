from google.appengine.ext import db
from google.appengine.ext import blobstore

class PanoramaStatus():
    NEW = 'NEW'
    THUMBNAIL = 'THUMBNAIL'
    TILES = 'TILES'
    LIVE = 'LIVE'
    ERROR = 'ERROR'

class Panorama(db.Model):
    owner = db.UserProperty(required=True)
    title = db.StringProperty(required=True)
    status = db.StringProperty(required=True, default=PanoramaStatus.NEW)
    statusText = db.StringProperty()
    thumbnail = db.BlobProperty()
    heading = db.FloatProperty(required=True, default=0.0)
    latitude = db.FloatProperty(required=True, default=50.12)
    longitude = db.FloatProperty(required=True, default=8.91)
    rawBlob = blobstore.BlobReferenceProperty(required=True)
    rawHeight = db.IntegerProperty()
    rawWidth = db.IntegerProperty()

    def statusDescription(self):
        if self.status == PanoramaStatus.NEW:
            return "Waiting for processing..."
        elif self.status == PanoramaStatus.THUMBNAIL:
            return "Generating thumbnail..."
        elif self.status == PanoramaStatus.TILES:
            return "Tiling image..."
        elif self.status == PanoramaStatus.LIVE:
            return "Live"
        elif self.status == PanoramaStatus.ERROR:
            return "Error processing panorama"
        else:
            return "Unknown status"

    def live(self):
        return self.status == PanoramaStatus.LIVE

class PanoramaTile(db.Model):
    data = db.BlobProperty(required=True)
    panoramaKey = db.ReferenceProperty(Panorama, required=True)
    position = db.StringProperty(required=True)
