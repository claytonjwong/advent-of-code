#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>


using namespace std;


enum class Attack
{
    Cold, Fire, Bludgeoning, Slashing, Radiation;
};
using Weaknesses = unordered_set< Attack >;
using Immunities = unordered_set< Attack >;

enum class GroupType
{
    immuneSystem, infection;
};


struct Group
{
    GroupType type; Attack attackType;
    int units{ 0 }, hitPoints{ 0 }, attackPower{ 0 }, initiative{ 0 };
    Weaknesses weaknesses;
    Immunities immunities;
};
using Groups = vector< Group >;


//Immune System:
//3321 units each with 6178 hit points (immune to bludgeoning, fire) with an attack that does 18 bludgeoning damage at initiative 20
//4228 units each with 9720 hit points (weak to bludgeoning) with an attack that does 21 fire damage at initiative 10
//1181 units each with 5833 hit points (weak to bludgeoning; immune to slashing, cold) with an attack that does 44 cold damage at initiative 6
//89 units each with 6501 hit points (weak to slashing, bludgeoning) with an attack that does 715 fire damage at initiative 1
//660 units each with 5241 hit points (weak to slashing) with an attack that does 75 radiation damage at initiative 11
//3393 units each with 3576 hit points (immune to cold, radiation; weak to fire) with an attack that does 9 fire damage at initiative 3
//2232 units each with 5558 hit points (immune to slashing) with an attack that does 21 fire damage at initiative 7
//4861 units each with 13218 hit points (weak to slashing, fire) with an attack that does 20 fire damage at initiative 14
//3102 units each with 7657 hit points (immune to cold; weak to slashing) with an attack that does 24 radiation damage at initiative 17
//8186 units each with 5664 hit points (weak to slashing) with an attack that does 6 bludgeoning damage at initiative 9
//
//Infection:
//931 units each with 32672 hit points (weak to slashing) with an attack that does 67 slashing damage at initiative 13
//1328 units each with 40275 hit points (immune to fire, radiation) with an attack that does 54 bludgeoning damage at initiative 5
//5620 units each with 43866 hit points (weak to radiation, fire) with an attack that does 12 cold damage at initiative 18
//3596 units each with 44288 hit points (immune to bludgeoning, fire) with an attack that does 22 slashing damage at initiative 8
//85 units each with 15282 hit points (weak to cold, fire) with an attack that does 272 fire damage at initiative 15
//129 units each with 49924 hit points (weak to bludgeoning) with an attack that does 681 radiation damage at initiative 4
//5861 units each with 24179 hit points (weak to slashing) with an attack that does 8 cold damage at initiative 16
//3132 units each with 5961 hit points (immune to radiation) with an attack that does 3 slashing damage at initiative 19
//1336 units each with 56700 hit points (weak to bludgeoning, radiation) with an attack that does 69 radiation damage at initiative 12
//2611 units each with 28641 hit points with an attack that does 21 fire damage at initiative 2

int main()
{
//    Groups G( 20 );
//
//    //3321 units each with 6178 hit points (immune to bludgeoning, fire) with an attack that does 18 bludgeoning damage at initiative 20
//    G[0].units = 3321, G[0].hitPoints = 6178, G[0].attackPower = 18, G[0].initiative = 20,
//    G[0].attackType = Attack::Bludgeoning,
//    G[0].immunities.insert( Attack::Bludgeoning ), G[0].immunities.insert( Attack::Fire );
//
//    //4228 units each with 9720 hit points (weak to bludgeoning) with an attack that does 21 fire damage at initiative 10
//    G[1].units = 4228, G[1].hitPoints = 9720, G[1].attackPower = 21, G[1].initiative = 10,
//    G[1].attackType = Attack::Fire,
//    G[1].weaknesses.insert( Attack::Bludgeoning );
//
//    //1181 units each with 5833 hit points (weak to bludgeoning; immune to slashing, cold) with an attack that does 44 cold damage at initiative 6
//    G[2].units = 1181, G[2].hitPoints = 5833, G[2].attackPower = 44, G[2].initiative = 6,
//    G[2].attackType = Attack::Fire,
//        G[2].weaknesses.insert( Attack::Bludgeoning );

    //89 units each with 6501 hit points (weak to slashing, bludgeoning) with an attack that does 715 fire damage at initiative 1
    //660 units each with 5241 hit points (weak to slashing) with an attack that does 75 radiation damage at initiative 11
    //3393 units each with 3576 hit points (immune to cold, radiation; weak to fire) with an attack that does 9 fire damage at initiative 3
    //2232 units each with 5558 hit points (immune to slashing) with an attack that does 21 fire damage at initiative 7
    //4861 units each with 13218 hit points (weak to slashing, fire) with an attack that does 20 fire damage at initiative 14
    //3102 units each with 7657 hit points (immune to cold; weak to slashing) with an attack that does 24 radiation damage at initiative 17
    //8186 units each with 5664 hit points (weak to slashing) with an attack that does 6 bludgeoning damage at initiative 9
    //
    //Infection:
    //931 units each with 32672 hit points (weak to slashing) with an attack that does 67 slashing damage at initiative 13
    //1328 units each with 40275 hit points (immune to fire, radiation) with an attack that does 54 bludgeoning damage at initiative 5
    //5620 units each with 43866 hit points (weak to radiation, fire) with an attack that does 12 cold damage at initiative 18
    //3596 units each with 44288 hit points (immune to bludgeoning, fire) with an attack that does 22 slashing damage at initiative 8
    //85 units each with 15282 hit points (weak to cold, fire) with an attack that does 272 fire damage at initiative 15
    //129 units each with 49924 hit points (weak to bludgeoning) with an attack that does 681 radiation damage at initiative 4
    //5861 units each with 24179 hit points (weak to slashing) with an attack that does 8 cold damage at initiative 16
    //3132 units each with 5961 hit points (immune to radiation) with an attack that does 3 slashing damage at initiative 19
    //1336 units each with 56700 hit points (weak to bludgeoning, radiation) with an attack that does 69 radiation damage at initiative 12
    //2611 units each with 28641 hit points with an attack that does 21 fire damage at initiative 2

    Groups G( 4 );

//    Immune System:
//    17 units each with 5390 hit points (weak to radiation, bludgeoning) with
//    an attack that does 4507 fire damage at initiative 2
    G[0].type = GroupType::immuneSystem, G[0].attackType = Attack::Fire,
    G[0].units = 17, G[0].hitPoints = 5390, G[0].attackPower = 4507, G[0].initiative = 2,
    G[0].weaknesses.insert( Attack::Radiation ), G[0].weaknesses.insert( Attack::Bludgeoning );

//    989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
//    slashing) with an attack that does 25 slashing damage at initiative 3
    G[1].type = GroupType::immuneSystem, G[1].attackType = Attack::Slashing,
    G[1].units = 989, G[1].hitPoints = 1274, G[1].attackPower = 25, G[1].initiative = 3,
    G[1].weaknesses.insert( Attack::Bludgeoning ), G[1].weaknesses.insert( Attack::Slashing ),
    G[1].immunities.insert( Attack::Fire );

//    Infection:
//    801 units each with 4706 hit points (weak to radiation) with an attack
//    that does 116 bludgeoning damage at initiative 1
    G[2].type = GroupType::infection, G[2].attackType = Attack::Bludgeoning,
    G[2].units = 801, G[2].hitPoints = 4706, G[2].attackPower = 116, G[2].initiative = 1,
    G[2].weaknesses.insert( Attack::Radiation );

//    4485 units each with 2961 hit points (immune to radiation; weak to fire,
//    cold) with an attack that does 12 slashing damage at initiative 4
    G[3].type = GroupType::infection, G[3].attackType = Attack::Slashing,
    G[3].units = 4485, G[3].hitPoints = 2961, G[3].attackPower = 12, G[3].initiative = 4,
    G[3].weaknesses.insert( Attack::Fire ), G[3].weaknesses.insert( Attack::Cold ),
    G[3].immunities.insert( Attack::Radiation );


    return 0;
}