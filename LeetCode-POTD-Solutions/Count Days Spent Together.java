class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        auto toDays = [](string date) {
            int month = stoi(date.substr(0, 2));
            int day = stoi(date.substr(3, 2));
            int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

            for (int i = 0; i < month - 1; i++) {
                day += days[i];
            }

            return day;
        };

        int start = max(toDays(arriveAlice), toDays(arriveBob));
        int end = min(toDays(leaveAlice), toDays(leaveBob));

        return max(0, end - start + 1);
    }
};