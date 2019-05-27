from django.http import Http404

class Projects():
    PROJECTS = [
        {
            'title': 'Animation Science',
            'subtitle': 'Experiment with CSS animations',
            'slug': 'animation-science',
            'cover': 'images/animation-science/0.png',
            'images': [
                'images/animation-science/0.png',
                'images/animation-science/1.png',
            ]
        },
        {
            'title': 'Canvas Piano',
            'subtitle': 'Piano game with canvas',
            'slug': 'canvas-piano',
            'cover': 'images/canvas-piano/0.png',
            'images': [
                'images/canvas-piano/0.png',
                'images/canvas-piano/1.png',
                'images/canvas-piano/2.png',
                'images/canvas-piano/3.png',
                'images/canvas-piano/4.png',
            ]
        },
        {
            'title': 'ChatMEAN',
            'subtitle': 'Chat app with Stack MEAN',
            'slug': 'chat-mean',
            'cover': 'images/chat-mean/0.png',
            'images': [
                'images/chat-mean/0.png',
                'images/chat-mean/1.png',
                'images/chat-mean/2.png',
                'images/chat-mean/3.png',
            ]
        },
        {
            'title': 'Clock',
            'subtitle': 'Clock with HTML/CSS/JS',
            'slug': 'clock',
            'cover': 'images/clock/0.png',
            'images': [
                'images/clock/0.png',
            ]
        },
        {
            'title': 'Gaëtan Lefebvre',
            'subtitle': 'Portfolio for Gaëtan Lefebvre with Nuxt.js',
            'slug': 'gaetan-lefebvre',
            'cover': 'images/gaetan-lefebvre/0.png',
            'images': [
                'images/gaetan-lefebvre/0.png',
                'images/gaetan-lefebvre/1.png',
                'images/gaetan-lefebvre/2.png',
                'images/gaetan-lefebvre/3.png',
                'images/gaetan-lefebvre/4.png',
                'images/gaetan-lefebvre/5.png',
                'images/gaetan-lefebvre/6.png',
                'images/gaetan-lefebvre/7.png',
                'images/gaetan-lefebvre/8.png',
                'images/gaetan-lefebvre/9.png',
                'images/gaetan-lefebvre/10.png',
                'images/gaetan-lefebvre/11.png',
            ]
        },
        {
            'title': 'Green Tips',
            'subtitle': 'Blog about environment with WordPress',
            'slug': 'green-tips',
            'cover': 'images/green-tips/0.png',
            'images': [
                'images/green-tips/0.png',
                'images/green-tips/1.png',
                'images/green-tips/2.png',
                'images/green-tips/3.png',
                'images/green-tips/4.png',
            ]
        },
        {
            'title': 'Loyalty',
            'subtitle': 'Card manager app with Swift',
            'slug': 'lopyalty',
            'cover': 'images/loyalty/0.png',
            'images': [
                'images/loyalty/0.png',
                'images/loyalty/1.png',
            ]
        },
        {
            'title': 'Mars Journey',
            'subtitle': 'Website with HTML/CSS/JS',
            'slug': 'mars-journey',
            'cover': 'images/mars-journey/0.png',
            'images': [
                'images/mars-journey/0.png',
                'images/mars-journey/1.png',
                'images/mars-journey/2.png',
                'images/mars-journey/3.png',
                'images/mars-journey/4.png',
                'images/mars-journey/5.png',
                'images/mars-journey/6.png',
                'images/mars-journey/7.png',
                'images/mars-journey/8.png',
                'images/mars-journey/9.png',
                'images/mars-journey/10.png',
            ]
        },
        {
            'title': 'Pokedex',
            'subtitle': 'Pokedex with Slim PHP',
            'slug': 'pokedex',
            'cover': 'images/pokedex/0.png',
            'images': [
                'images/pokedex/0.png',
                'images/pokedex/1.png',
                'images/pokedex/2.png',
                'images/pokedex/3.png',
                'images/pokedex/4.png',
                'images/pokedex/5.png',
                'images/pokedex/6.png',
            ]
        },
        {
            'title': 'Raining molecules',
            'subtitle': 'Drawing with canvas',
            'slug': 'raining-molecules',
            'cover': 'images/raining-molecules/0.png',
            'images': [
                'images/raining-molecules/0.png',
            ]
        },
        {
            'title': 'Scaneat',
            'subtitle': 'Food app with Swift',
            'slug': 'scaneat',
            'cover': 'images/scaneat/0.png',
            'images': [
                'images/scaneat/0.png',
                'images/scaneat/1.png',
            ]
        },
        {
            'title': 'Todo list',
            'subtitle': 'Todo list with PHP',
            'slug': 'todo-list',
            'cover': 'images/todo-list/0.png',
            'images': [
                'images/todo-list/0.png',
                'images/todo-list/1.png',
                'images/todo-list/2.png',
                'images/todo-list/3.png',
                'images/todo-list/4.png',
            ]
        },
    ]

    @classmethod
    def all(self):
        return self.PROJECTS

    @classmethod
    def find(self, slug):
        for _project in self.PROJECTS:
            if _project['slug'] == slug:
                return _project

        raise Http404('Project not found')
