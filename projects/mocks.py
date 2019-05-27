from django.http import Http404

class Projects():
  PROJECTS = [
    {'id': 1, 'title': 'First', 'slug': 'first'},
    {'id': 2, 'title': 'Second', 'slug': 'second'},
    {'id': 3, 'title': 'Third', 'slug': 'third'},
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
