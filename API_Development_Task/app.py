from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

reviews = []

class MovieReview(Resource):
    def get(self, review_id):
        review = next((rev for rev in reviews if rev['id'] == review_id), None)
        if review:
            return jsonify(review)
        return {'message': 'Review not found'}, 404

    def put(self, review_id):
        review = next((rev for rev in reviews if rev['id'] == review_id), None)
        if not review:
            return {'message': 'Review not found'}, 404
        data = request.get_json()
        review['movie_title'] = data.get('movie_title', review['movie_title'])
        review['review'] = data.get('review', review['review'])
        review['rating'] = data.get('rating', review['rating'])
        review['date'] = data.get('date', review['date'])
        return jsonify(review)

    def delete(self, review_id):
        review = next((rev for rev in reviews if rev['id'] == review_id), None)
        if not review:
            return {'message': 'Review not found'}, 404
        reviews.remove(review)
        return {'message': 'Review deleted'}, 200

class ReviewList(Resource):
    def get(self):
        return jsonify(reviews)

    def post(self):
        data = request.get_json()
        review_id = len(reviews) + 1
        review = {
            'id': review_id,
            'movie_title': data['movie_title'],
            'review': data['review'],
            'rating': data['rating'],
            'date': data['date']
        }
        reviews.append(review)
        return jsonify(review), 201

api.add_resource(ReviewList, '/reviews')
api.add_resource(MovieReview, '/reviews/<int:review_id>')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
