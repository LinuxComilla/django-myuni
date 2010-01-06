import settings

def handle_uploaded_file(f, obj):
	filename = ''.join(obj.pk, os.path.splitext(f.name)[1])
	destination = open(os.path.join(settings.UPLOADS_PATH, filename), 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
