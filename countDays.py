
def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

    days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]


    def date_to_day(day_str:str)->int:
       
        month,day = map(int, day_str.split("-"))

        return sum(days_in_months[:month - 1]) + day


    a_alice = date_to_day(arriveAlice)
    l_alice = date_to_day(leaveAlice)
    a_bob = date_to_day(arriveBob)
    l_bob = date_to_day(leaveBob)

    start = max(a_alice,a_bob)
    end = min(l_alice,l_bob)

    days_overlap = end - start + 1

    return days_overlap



#t.c -> o(1) , s.c-> O(1)
class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    # 1. Precomputed table
    prefix_days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

 
    def to_day(date_str: str) -> int:
      m = int(date_str[:2])
      d = int(date_str[3:])
      return prefix_days[m] + d

    # 3. Charon dates ko Day 1..365 me badal lo
    start = max(to_day(arriveAlice), to_day(arriveBob))
    end = min(to_day(leaveAlice), to_day(leaveBob))

    # 4. Overlap result
    if start <= end:
      return end - start + 1
    return 0

