from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    '''
    function index: index page view data
    Parameters
    ----------
    none
    Return
    -------
    render
    '''
    return render(request, 'pages/index.html.jinja', {
        'h1': 'Alain Cao Van Truong',
        'h2': 'Full-stack developer & web student',
    })

def about(request):
    '''
    function about: about page view data
    Parameters
    ----------
    none
    Return
    -------
    render
    '''
    return render(request, 'pages/about.html.jinja', {
        'h1': 'About myself',
        'h2': 'Learn about what I like doing',
        'skills': [
            'Vue.js',
            'Nuxt.js',
            'PHP Slim',
            'Swift',
            'Three.js',
            'Sass',
            'Stylus',
            'Pug',
            'Typescript',
            'Node.js',
            'AngularJS',
            'React.js',
            'Laravel',
            'WordPress',
            'Django',
            'Ruby on Rails',
        ]
    })

def contact(request):
    '''
    function contact: contact page view data
    Parameters
    ----------
    none
    Return
    -------
    render
    '''
    return render(request, 'pages/contact.html.jinja', {
        'h1': 'Contact me',
        'h2': 'See how to find me',
    })

def error404(request, exception=None):
    '''
    function error404: error 404 page view data
    Parameters
    ----------
    none
    Return
    -------
    render
    '''
    return render(request, 'errors/404.html.jinja', {'error': exception}, status=404)
