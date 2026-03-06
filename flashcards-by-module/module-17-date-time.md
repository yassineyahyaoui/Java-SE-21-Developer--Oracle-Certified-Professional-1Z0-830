# Module 17 -- Date&Time

### Q: What is LocalDate and which package is it in?
LocalDate is an immutable date-time object representing a date (year-month-day) without time or time zone. It is in java.time and is thread-safe.

### Q: How do you get the current date and create a specific date with LocalDate?
Current: `LocalDate.now()`. Specific: `LocalDate.of(year, month, day)` or `LocalDate.of(year, Month.JULY, day)` using the Month enum.

### Q: What is LocalTime?
LocalTime is an immutable time-only type (hour, minute, second, nanosecond) without date or time zone. Create with `LocalTime.now()` or `LocalTime.of(hour, minute, second)`.

### Q: What is LocalDateTime?
LocalDateTime combines date and time without time zone. Use when you need both date and time in a single value (e.g. LocalDate + LocalTime).

### Q: What is Period and what is it used for?
Period is a date-based amount (years, months, days). Use it with LocalDate for date-only math (e.g. adding 2 weeks to a date). Created with Period.ofDays(n), Period.of(years, months, days), or between two LocalDates.

### Q: What is Duration and how does it differ from Period?
Duration is time-based (hours, minutes, seconds, nanos). Use it with Instant, LocalTime, or LocalDateTime for time-based amounts. Period is for dates (years, months, days); Duration is for time.

### Q: What is DateTimeFormatter and how do you use it?
DateTimeFormatter formats and parses date-time objects. Use with format() and parse(): `LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE)` or parse a string with `LocalDate.parse("2024-01-15", formatter)`.

### Q: Is the old Calendar class mutable or immutable?
Calendar is mutable. The java.time API (LocalDate, LocalTime, etc.) is immutable and preferred for new code.
