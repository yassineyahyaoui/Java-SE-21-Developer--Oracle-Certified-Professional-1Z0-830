# Day 30 -- Date and Time (Part 1)

### Q: How do you obtain an instance of the Calendar class?
Use the static method `Calendar.getInstance()`. Calendar is abstract, so you cannot use a constructor; getInstance() returns a Calendar instance based on the current time in the default time zone and locale.

### Q: Is the Calendar class mutable or immutable?
Calendar is mutable. Once created, Calendar objects can be modified (e.g. with set, add). For immutable date-time behavior, use the java.time API (LocalDate, LocalTime, etc.).

### Q: How do you get the current year and month from a Calendar?
Use `calendar.get(Calendar.YEAR)` and `calendar.get(Calendar.MONTH)`. get(int field) returns the value for the given field constant. Store results in int variables.

### Q: Why is Calendar.MONTH zero-based?
Months are 0–11: January = 0, September = 8, December = 11. This is similar to zero-based list indices and is a common source of off-by-one errors if you forget.

### Q: What is the difference between Calendar.HOUR and Calendar.HOUR_OF_DAY?
HOUR is 12-hour (0–11; noon and midnight are 0). HOUR_OF_DAY is 24-hour (0–23). Use HOUR_OF_DAY when you need 24-hour time.

### Q: How do you get a Date from a Calendar?
Use `calendar.getTime()`. It returns a Date object representing the calendar’s current time. You can then format it with SimpleDateFormat.

### Q: What is LocalDate and which package is it in?
LocalDate is an immutable date-time object representing a date (year-month-day) without time or time zone in the ISO-8601 calendar. It is in the java.time package and is thread-safe.

### Q: How do you get the current date with LocalDate?
Use `LocalDate.now()`. There is no public constructor; use static factory methods such as now() and of().

### Q: How do you create a specific date with LocalDate?
Use `LocalDate.of(year, month, day)` with int month, or `LocalDate.of(year, Month.JULY, day)` using the Month enum. Example: `LocalDate.of(2014, 7, 15)` or `LocalDate.of(2014, Month.JULY, 15)`.

### Q: How do you get year and month from a LocalDate?
Use `localDate.getYear()` and `localDate.getMonth()`. getMonth() returns a Month enum; you can also use getMonthValue() for the numeric month (1–12).

### Q: How do you compare two LocalDate values?
Use `date1.isAfter(date2)` and `date1.isBefore(date2)`. Both return boolean. Useful for anniversaries or any before/after date logic.

### Q: What is LocalTime and how is it used?
LocalTime is an immutable time-only type (hour, minute, second, nanosecond) without date or time zone in ISO-8601. It represents “wall clock” time and is in java.time.

### Q: Does LocalTime have a public constructor?
No. LocalTime has no public constructor and is final. Create instances via static factory methods such as `LocalTime.now()` and `LocalTime.of(hour, minute, second)`.

### Q: How do you get the current time and its components with LocalTime?
Use `LocalTime.now()` for current time. Use `getHour()`, `getMinute()`, `getSecond()`, and `getNano()` to get individual components.

### Q: Is LocalTime immutable?
Yes. Once created, a LocalTime instance does not change. Methods like plusHours or minusMinutes return a new LocalTime; they do not modify the original.

### Q: What do all java.time classes (LocalDate, LocalTime, etc.) have in common regarding design?
They are immutable, thread-safe, and final, with no public constructors. You use static factory methods (now(), of(), etc.) to create instances.

### Q: What parameter ranges does LocalTime.of(hour, minute, second) expect?
Hour 0–23, minute 0–59, second 0–59. Values outside these ranges throw DateTimeException.
