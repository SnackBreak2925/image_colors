try:
    from app import app as backend
    import unittest
except Exception as e:
    raise Exception("Miss packages for test {}".format(e))


class TestBackend(unittest.TestCase):

    base64_string = '''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
    gGWDJSghKgd8QAAAABJRU5ErkJggg=='''

    # test 405 for get to /proccess_image
    def test_get(self):
        self.backend = backend.test_client()
        response = self.backend.get("/proccess_image")
        status_code = response.status_code
        self.assertEqual(status_code, 405)

    # test 400 for post without file to /proccess_image
    def test_fileless(self):
        self.backend = backend.test_client()
        response = self.backend.post("/proccess_image", json={
            "countColor": 12
        })
        status_code = response.status_code
        self.assertEqual(status_code, 400)

    # test 400 for post without colors counter to /proccess_image
    def test_no_colors(self):
        self.backend = backend.test_client()
        response = self.backend.post("/proccess_image", json={
            "file": self.base64_string,
        })
        status_code = response.status_code
        self.assertEqual(status_code, 400)

    # test 200 for right post to /proccess_image
    def test_success(self):
        self.backend = backend.test_client()
        response = self.backend.post("/proccess_image", json={
            "file": self.base64_string,
            "countColor": 12
        })
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check data application/json for right post to /proccess_image
    def test_json(self):
        self.backend = backend.test_client()
        response = self.backend.post("/proccess_image", json={
            "file": self.base64_string,
            "countColor": 12
        })
        self.assertEqual(response.content_type, "application/json")

    # check data for right post to /proccess_image is array of hexes
    def test_array(self):
        self.backend = backend.test_client()
        response = self.backend.post("/proccess_image", json={
            "file": self.base64_string,
            "countColor": 12
        })
        data = response.get_json()
        for i in data:
            self.assertRegex(i, r"#[0-9A-F]{6}")
        self.assertEqual(type(data), type([]))

    if __name__ == "__main__":
        unittest.main()
