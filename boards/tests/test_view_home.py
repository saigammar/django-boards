from django.test import TestCase
from django.urls import reverse,resolve
from ..models import Board
from ..views import BoardListView


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    #def test_home_url_resolves_home_view(self):
    #    view = resolve('/')
    #    self.assertEquals(view.func, home)
    '''below is a test case for class based view as opposed to the above one that is for function based '''
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    # to test links from home page to topic pages.
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url=reverse('board_topics',kwargs={'pk':self.board.pk})
        self.assertContains(self.response,'href="{0}"'.format(board_topics_url))