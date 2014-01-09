from django.utils import simplejson
                                            RepositoryError,
                                            TwoFactorAuthCodeRequiredError)
                                 '%(github_public_repo_name)s/issues#issue/%%s',
    supports_bug_trackers = True
    supports_two_factor_auth = True
        except Exception, e:
                  two_factor_auth_code=None, local_site_name=None,
                  *args, **kwargs):
            headers = {}

            if two_factor_auth_code:
                headers['X-GitHub-OTP'] = two_factor_auth_code

                headers=headers,
                body=simplejson.dumps(body))
        except (urllib2.HTTPError, urllib2.URLError), e:
                rsp = simplejson.loads(data)
                response_info = e.info()
                x_github_otp = response_info.get('X-GitHub-OTP', '')

                if x_github_otp.startswith('required;'):
                    raise TwoFactorAuthCodeRequiredError(
                        _('Enter your two-factor authentication code '
                          'and re-enter your password to link your account. '
                          'This code will be sent to you by GitHub.'))

            return simplejson.loads(data)
        except (urllib2.URLError, urllib2.HTTPError), e:
                rsp = simplejson.loads(data)