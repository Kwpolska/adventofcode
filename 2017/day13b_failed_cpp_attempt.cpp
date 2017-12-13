#include <iostream>
#include <vector>

#define UP -1
#define DOWN 1

using namespace std;

class Layer {
    public:
        int number;
        int range;
        int position = 0;
        int direction = DOWN;

        Layer(int number, int range, int position=0, int direction=DOWN):
            number(number), range(range), position(position), direction(direction) {} /* {
            this->number = number;
            this->range = range;
        }*/

        Layer(const Layer&) = default;
        /*{
            this->number = rhs.number;
            this->range = rhs.range;
            this->position = rhs.position;
            this->direction = rhs.direction;
        }*/

        void step();
        int check();
        void print();
};

void Layer::step() {
    if (range == -1) return;
    position += direction;
    if (position >= (range - 1) || position == 0) {
        direction *= -1;
    }
}

int Layer::check() {
    if (range == -1 || position != 0) return 0;
    return 1;
}

void Layer::print() {
    cout << number << " " << range << " " << position << " " << direction << endl;
}

int main() {
    int num_layers, number, range;
    cin >> num_layers;
    vector<Layer> layers_original;
    for (int i = 0; i < num_layers; i++) {
        cin >> number;
        cin >> range;
        layers_original.push_back(Layer(number, range, 0, DOWN));
    }

    vector<Layer> layers_current = layers_original;

    /*
    for (int i = 0; i < num_layers; i++) {
        layers_original[i].print();
        layers_current[i].print();
    }*/

    int wait = 0;
    int failure = 1;
    while (failure > 0) {
        cerr << "\r" << wait;
        ++wait;
        failure = 0;

        for (Layer l: layers_current) {
            l.step();
            //l.print();
        }

        vector<Layer> layers_test = layers_current;

        for (Layer lc: layers_test) {
            //lc.print();
            failure += lc.check();
            if (failure) continue;
            for (Layer l: layers_test) {
                l.step();
            }
        }
    }
    cout << "\n\nANSWER:\n" << wait << endl;
    return 0;
}
