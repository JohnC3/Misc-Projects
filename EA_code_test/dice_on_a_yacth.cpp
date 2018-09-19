#include <iostream>

#define anum 1;

#define NUM_DICE 5
#define DICE_SIDES 8

using namespace std;

enum Category {Ones,
  Twos, Threes, Fours, Fives, Sizes, Sevens, Eights,
  ThreeOfAKind, FourOfAKind, FullHouse,
  SmallStraight, LargeStraight,
  AllDifferent, Chance, AllSame};


bool simple_in(int array[], int val, int size){
  // Return true if val in array

  for (int i = 0; i < size + 1; i++){
    if (array[i] == val) {
      return true;
    }
  }
  return false;

}


bool simple_least(int array[], int val, int size){
  // Returns true if val or something bigger is in the array
  for (int i = 0; i < size + 1; i++){
    if (array[i] >= val) {
      return true;
    }
  }
  return false;
}


int *dice_count(int *output, int dice[], int size){
  // count the number of occurances of each dice value and store it in output
  int val;
  for (int i = 0; i < size; i++){
    val = dice[i];
    if (val != 0){
      output[val] += 1;
    }
  }
  return output;
};


int straight_length(int count_arr[]){
  // Returns longest straight
  int longest = 0;
  int current_straight = 0;

  for (int i = 0; i <= DICE_SIDES + 1; i++){

    if (count_arr[i] > 0){
      current_straight += 1;
    }
    else{

      if (current_straight > longest){
        longest = current_straight;
        current_straight = 0;
      }
    }

  }
  if (current_straight > longest){
    longest = current_straight;
  }
  return longest;
}


int sum(int dice[NUM_DICE]){
  int score = 0;
  for (int i = 0; i < NUM_DICE; i++){
      score += dice[i];
  };
  return score;
};


int scoreMatches(int dice[NUM_DICE], int catagory) {
    catagory += 1;
    int score = 0;
    for(int i = 0; i < NUM_DICE; i++){
      if(dice[i] == catagory){
        score += catagory;
      }
    };
    return score;
};


int getScore (int dice[NUM_DICE], int catagory){
    // cout << "Running get score catagory: " << catagory << endl;
    // catagory 0 - 7 handle the basic add up matching values catagory
    if(catagory <= Eights){
      return scoreMatches(dice, catagory);
    }
    // Keep track of the count of dice values
    int dice_count_array[DICE_SIDES + 1];
    std::fill_n(dice_count_array, DICE_SIDES + 1, 0);
    dice_count(dice_count_array, dice, NUM_DICE);
    // And the count of counts of dice values
    int count_count[DICE_SIDES + 1];
    std::fill_n(count_count, DICE_SIDES + 1, 0);
    dice_count(count_count, dice_count_array, DICE_SIDES);

    switch (catagory) {
      case ThreeOfAKind:
        if (simple_least(dice_count_array, 3, DICE_SIDES)){
          return sum(dice);
        }
        break;
      case FourOfAKind:
        if (simple_least(dice_count_array, 4, DICE_SIDES)){
          return sum(dice);
        }
        break;

      case FullHouse:
        if (simple_in(dice_count_array, 3, DICE_SIDES) && simple_in(dice_count_array, 2, DICE_SIDES)){
          return 25;
        }
        break;
      case SmallStraight:
        if (straight_length(dice_count_array) >= 4){
          return 30;
        }
        break;
      case LargeStraight:
        if (straight_length(dice_count_array) >= 5){
          return 40;
        }
        break;
      case AllDifferent:
        if (count_count[1] == 5){
          return 40;
        }
        break;
      case Chance:
        return sum(dice);
      case AllSame:
        if (simple_in(dice_count_array, NUM_DICE, DICE_SIDES)){
          return 50;
        }
        break;

    }

    return 0;
}

int main()
{
    int testval_1[5] = {1, 2, 3, 4, 5};
    cout << "[1, 2, 3, 4, 5]: SmallStraight " << getScore(testval_1, SmallStraight) << endl;
    cout << "[1, 2, 3, 4, 5]: LargeStraight " << getScore(testval_1, LargeStraight) << endl;
    cout << "[1, 2, 3, 4, 5]: AllDifferent " << getScore(testval_1, AllDifferent) << endl;
    cout << "[1, 2, 3, 4, 5]: Chance " << getScore(testval_1, Chance) << endl;


    int testval_2[5] = {2, 2, 3, 3, 3};
    cout << "{2, 2, 3, 3, 3}: FullHouse " << getScore(testval_2, FullHouse) << endl;
    cout << "{2, 2, 3, 3, 3}: ThreeOfAKind " << getScore(testval_2, ThreeOfAKind) << endl;

    int testval_3[5] = {2, 2, 2, 2, 2};
    cout << "{2, 2, 2, 2, 2}: AllSame " << getScore(testval_3, AllSame) << endl;
    cout << "{2, 2, 2, 2, 2}: FourOfAKind " << getScore(testval_3, FourOfAKind) << endl;



    int test_val_4[5] = {1, 2, 3, 4, 1};
    cout << "{1, 2, 3, 4, 1}: Ones " << getScore(test_val_4, Ones) << endl;

    return 0;
}
