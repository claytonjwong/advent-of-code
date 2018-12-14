#include "Input.hpp"
#include "Director.hpp"
#include "Cart.hpp"
#include "Model.hpp"
#include <iostream>


using namespace std;


int main() {

    Model model{ INPUT };
    while ( ! model.isCollision() )
    {
        model.tick();
    }

    cout << model.getCollisionPosition() << endl; // (14,42)

    return 0;
}
