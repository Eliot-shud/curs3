from utils import load_post


def test_posts(client):
    response = client.get('/api/post/')
    assert isinstance(response.json, list)
    assert response.status_code == 200


def test_post(client, posts_keys):
    response = client().get('/api/post/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert (response.json.keys()) == posts_keys

    def test_utils(posts_keys):
        response = load_post(1)
        assert isinstance(response.json, list)
        assert response.status_code == 200
