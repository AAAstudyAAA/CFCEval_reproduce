def try_post(self, request):
    try:
        zones = cgi.FieldStorage(fp=request.content, headers=request.
            getAllHeaders(), environ={'REQUEST_METHOD': 'POST',
            'CONTENT_TYPE': request.getAllHeaders()['content-type']})
        key = request.args.get('token', None)[0]
        fmt = request.args.get('fmt', None)[0]
        if fmt not in ['authenticode']:
            raise Exception('Unsupported token type for POST.')
        canary = Canarydrop(**get_canarydrop(canarytoken=key))
        if not canary:
            raise NoCanarytokenPresent()
        if fmt == 'authenticode':
            docname = zones['file_for_signing'].filename
            docbody = zones['file_for_signing'].value
            if len(docbody) > int(settings.MAX_UPLOAD_SIZE):
                response['Error'] = 4
                response['Message'
                    ] = 'File too large. File size must be < ' + str(int(
                    settings.MAX_UPLOAD_SIZE) / (1024 * 1024)) + 'MB.'
                raise Exception('File too large')
            if not docname.lower().endswith(('exe', 'dll')):
                raise Exception(
                    'Uploaded authenticode file must be an exe or dll')
            sign_bodies = make_canary_authenticode_binary(hostname=canary.
                get_hostname(with_random=False, as_url=True), filebody=docbody)
            request.setHeader('Content-Type', 'octet/stream')
            request.setHeader('Content-Disposition',
                'attachment; filename={filename}.signed'.format(filename=
                docname))
            return sign_bodies
    except Exception as e:
        log.error('Unexpected error in POST download: {err}'.format(err=e))
        frame = unsafe_env.get_template('error.html')
        return frame.render(error=e.message).encode('utf8')
    return NoResource().render(request)
