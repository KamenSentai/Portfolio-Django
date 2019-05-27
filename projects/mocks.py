from django.http import Http404

class Projects():
  PROJECTS = [
    {'title': 'Animation Science', 'subtitle': '', 'slug': 'animation-science', 'cover': 'images/animation-science/0.png'},
    {'title': 'Canvas Piano', 'subtitle': '', 'slug': 'canvas-piano', 'cover': 'images/canvas-piano/0.png'},
    {'title': 'ChatMEAN', 'subtitle': '', 'slug': 'chat-mean', 'cover': 'images/chat-mean/0.png'},
    {'title': 'Clock', 'subtitle': '', 'slug': 'clock', 'cover': 'images/clock/0.png'},
    {'title': 'Gaëtan Lefebvre', 'subtitle': '', 'slug': 'geatan-lefebvre', 'cover': 'images/gaetan-lefebvre/0.png'},
    {'title': 'Green Tips', 'subtitle': '', 'slug': 'green-tips', 'cover': 'images/green-tips/0.png'},
    {'title': 'Loyalty', 'subtitle': '', 'slug': 'lopyalty', 'cover': 'images/loyalty/0.png'},
    {'title': 'Mars Journey', 'subtitle': '', 'slug': 'mars-journey', 'cover': 'images/mars-journey/0.png'},
    {'title': 'Pokedex', 'subtitle': '', 'slug': 'pokedex', 'cover': 'images/pokedex/0.png'},
    {'title': 'Raining molecules', 'subtitle': '', 'slug': 'raining-molecules', 'cover': 'images/raining-molecules/0.png'},
    {'title': 'Scaneat', 'subtitle': '', 'slug': 'scaneat', 'cover': 'images/scaneat/0.png'},
    {'title': 'Todo list', 'subtitle': '', 'slug': 'todo-list', 'cover': 'images/todo-list/0.png'},
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
