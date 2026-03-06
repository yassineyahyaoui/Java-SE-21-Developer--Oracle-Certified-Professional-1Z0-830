# Module 17 -- Date&Time

### Q: How do you use the legacy `Calendar` class: obtain an instance with `Calendar.getInstance()` and extract fields with `calendar.get(Calendar.YEAR)`, `.MONTH`, `.WEEK_OF_YEAR`, `.DAY_OF_MONTH`, etc.?

Use the legacy `Calendar` class: obtain an instance with `Calendar.getInstance()` and extract fields with `calendar.get(Calendar.YEAR)`, `.MONTH`, `.WEEK_OF_YEAR`, `.DAY_OF_MONTH`, etc.

### Q: Create `LocalDate` objects (`java.time`): immutable, date-only (year-month-day), no time or timezone, ISO-8601, thread-safe; use `LocalDate.now()`, `getYear()`, `getMonth()`?

Create `LocalDate` objects (`java.time`): immutable, date-only (year-month-day), no time or timezone, ISO-8601, thread-safe; use `LocalDate.now()`, `getYear()`, `getMonth()`

### Q: Create `LocalTime` objects (`java.time`): immutable, time-only (hour-minute-second), no date or timezone, ISO-8601, thread-safe, no public constructor, static factory methods?

Create `LocalTime` objects (`java.time`): immutable, time-only (hour-minute-second), no date or timezone, ISO-8601, thread-safe, no public constructor, static factory methods

### Q: What is that all `java.time` classes are immutable?

Explain that all `java.time` classes are immutable and final with no public constructors -- instances are created via static factory methods

### Q: Create `LocalDateTime` objects (`java.time`): combination of `LocalDate` and `LocalTime`, date + time without timezone, immutable, thread-safe, static factory methods?

Create `LocalDateTime` objects (`java.time`): combination of `LocalDate` and `LocalTime`, date + time without timezone, immutable, thread-safe, static factory methods

### Q: How do you use the `Period` class to represent a date-based amount of time in years, months, and days; create with `Period.of()` and `Period.between()`; apply to `LocalDate` for date arithmetic?

Use the `Period` class to represent a date-based amount of time in years, months, and days; create with `Period.of()` and `Period.between()`; apply to `LocalDate` for date arithmetic

### Q: How do you use the `Duration` class to represent a time-based amount in hours, minutes, seconds, and nanos; explain that `Duration` works with `LocalTime`/`LocalDateTime`/`Instant` but NOT with `LocalDate`?

Use the `Duration` class to represent a time-based amount in hours, minutes, seconds, and nanos; explain that `Duration` works with `LocalTime`/`LocalDateTime`/`Instant` but NOT with `LocalDate`

### Q: Format and parse date-time objects using `DateTimeFormatter` with custom patterns (`ofPattern`); use predefined formatters (`ISO_LOCAL_DATE`, `ISO_LOCAL_DATE_TIME`); explain that `DateTimeFormatter` replaces `SimpleDateFormat`?

Format and parse date-time objects using `DateTimeFormatter` with custom patterns (`ofPattern`); use predefined formatters (`ISO_LOCAL_DATE`, `ISO_LOCAL_DATE_TIME`); explain that `DateTimeFormatter` replaces `SimpleDateFormat`

### Q: Convert between time zones using `ZonedDateTime.withZoneSameInstant()` and explain DST edge cases (e.g., spring-forward: 2:00 AM does not exist)?

Convert between time zones using `ZonedDateTime.withZoneSameInstant()` and explain DST edge cases (e.g., spring-forward: 2:00 AM does not exist)

### Q: What is if you're paying attention year?

So if you're paying attention year is a static field defined in the calendar class.

### Q: What is The second?

The second is a current month, September, but it is the int value.

### Q: What is The next output?

The next output is the number of the week in the current year.

### Q: What is And the last output?

And the last output is the number of the day in the current week.

### Q: What is the first parameter of this method?

Now the first parameter of this method is the year value.

### Q: What is The second parameter?

The second parameter is the month value.

### Q: What is Anyway, what I do want to show you, though?

Anyway, what I do want to show you, though, is the mutability of the calendar class.

### Q: What is instead it?

So instead it is a description of the date like what you use for birthdays.

### Q: What is Well, the first output?

Well, the first output is the current date.

### Q: What is The second output?

The second output is the current year.

### Q: What is The third output?

The third output is the value of the current month.

### Q: What is Also, the local time class doesn't have any construc...?

Also, the local time class doesn't have any constructor and it is a final class just like the local day class.

### Q: What is Also, the part after the second?

Also, the part after the second refers to the nanosecond.

### Q: What is The first output?

The first output is the current time.

### Q: What is Second output?

Second output is the current hour.

### Q: What is Third output?

Third output is the current minute.

### Q: What is Next output?

Next output is the current second.

### Q: What is Last output?

Last output is the current nanosecond.

### Q: What is the local date time class?

So the local date time class is an immutable date time object that represents a date time often viewed as a year month day hour minute second.

### Q: What is after the letter T versus the hour, then the minute,...?

So after the letter T versus the hour, then the minute, then the second and last up is the nanosecond.

### Q: What is The period class doesn't have any constructor and it?

The period class doesn't have any constructor and it is a final class.

### Q: What is The upper left hand section?

The upper left hand section is a section with all the packages.

### Q: What is But this?

But this is the section where you'll see all the explanations about this package and the classes in the package.

### Q: What is There you see the ISO date time format?

There you see the ISO date time format is the same as the default format style.
