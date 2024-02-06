class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum([count.count_words() for count in self.entries])

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return int(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        closest_time = 0
        closest_entry = None
        for entry in self.entries:
            current = entry.reading_time(wpm)
            if current == minutes:
                return entry
            elif current < minutes and current > closest_time:
                closest_time = current
                closest_entry = entry
        if not closest_entry:
            return "No suitable entry!"
        return closest_entry



        
        
        # suitable = [entry for entry in self.entries if entry.reading_time(wpm) <= minutes]
        # suitable = [entry for entry in self.entries if entry.reading_time(wpm) <= minutes]
        # if len(suitable) == 0:
            # return "No suitable entries!"
        # return suitable[0]
