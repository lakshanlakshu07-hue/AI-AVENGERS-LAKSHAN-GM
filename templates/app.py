from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = [None] * total_slots

    def get_status(self):
        status = []
        for i in range(self.total_slots):
            status.append({
                'slot': i + 1,
                'available': self.slots[i] is None,
                'vehicle': self.slots[i] if self.slots[i] else None
            })
        return status

    def park_vehicle(self, vehicle_number):
        for i in range(self.total_slots):
            if self.slots[i] is None:
                self.slots[i] = vehicle_number
                return {'success': True, 'slot': i + 1, 'message': f'Vehicle {vehicle_number} parked at slot {i + 1}'}
        return {'success': False, 'message': 'Sorry! Parking lot is full.'}

    def remove_vehicle(self, vehicle_number):
        for i in range(self.total_slots):
            if self.slots[i] == vehicle_number:
                self.slots[i] = None
                return {'success': True, 'slot': i + 1, 'message': f'Vehicle {vehicle_number} removed from slot {i + 1}'}
        return {'success': False, 'message': 'Vehicle not found.'}

# Initialize parking lot with 5 slots
parking = ParkingLot(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    return jsonify(parking.get_status())

@app.route('/api/park', methods=['POST'])
def park_vehicle():
    data = request.get_json()
    vehicle_number = data.get('vehicle_number')
    if not vehicle_number:
        return jsonify({'success': False, 'message': 'Vehicle number is required'})
    
    result = parking.park_vehicle(vehicle_number)
    return jsonify(result)

@app.route('/api/remove', methods=['POST'])
def remove_vehicle():
    data = request.get_json()
    vehicle_number = data.get('vehicle_number')
    if not vehicle_number:
        return jsonify({'success': False, 'message': 'Vehicle number is required'})
    
    result = parking.remove_vehicle(vehicle_number)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
