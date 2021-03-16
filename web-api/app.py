from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/appearance', methods=['POST'])
def appearance():
    intervals = request.json['intervals']
    lesson = set()
    pupil = set()
    tutor = set()

    for el, el1 in zip(intervals['lesson'][::2], intervals['lesson'][1::2]):
        lesson.update(range(el, el1 + 1))
    for el, el1 in zip(intervals['pupil'][::2], intervals['pupil'][1::2]):
        pupil.update(range(el, el1 + 1))
    for el, el1 in zip(intervals['tutor'][::2], intervals['tutor'][1::2]):
        tutor.update(range(el, el1 + 1))

    return jsonify(
        {'appearance': len(lesson & pupil & tutor),
         'success ': True}
    ), 201


if __name__ == '__main__':
    app.run()
