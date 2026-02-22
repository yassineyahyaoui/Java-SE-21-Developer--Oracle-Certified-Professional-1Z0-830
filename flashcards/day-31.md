# Day 31 -- Date and Time (Part 2)

### Q: What is LocalDateTime and how does it relate to LocalDate and LocalTime?
LocalDateTime is an immutable date-time object that combines date and time (year, month, day, hour, minute, second, nanosecond) without time zone in ISO-8601. Think of it as LocalDate + LocalTime; it is in java.time and is thread-safe.

### Q: How do you create a LocalDateTime for “now” and for a specific date-time?
Use `LocalDateTime.now()` for the current date-time. Use `LocalDateTime.of(year, month, dayOfMonth, hour, minute)` or overloads, or `LocalDateTime.of(localDate, localTime)`.

### Q: Does LocalDateTime have a public constructor?
No. LocalDateTime is final with no public constructor. Use static methods such as now() and of() to create instances.

### Q: What is the Period class and what units does it support?
Period models a date-based amount of time in the ISO-8601 calendar: years, months, and days. It is immutable and thread-safe and is in java.time.

### Q: How do you create a Period and find the period between two dates?
Use `Period.of(years, months, days)` for a specific period. Use `Period.between(startDate, endDate)` where both are LocalDate. Example: `Period.between(birthDate, LocalDate.now())`.

### Q: Does Period work with LocalDate, LocalTime, or both?
Period is date-based and works with LocalDate (e.g. addTo/subtractFrom LocalDate, or between two LocalDates). It does not work with time-only types like LocalTime.

### Q: What is the Duration class and how does it differ from Period?
Duration models a time-based amount (hours, minutes, seconds, nanoseconds). It works with LocalTime, LocalDateTime, and Instant. Unlike Period, it does not work with LocalDate alone.

### Q: With which types can you use Duration?
Duration works with LocalTime, LocalDateTime, and Instant. It does not represent calendar date amounts and is not used with LocalDate alone.

### Q: What is DateTimeFormatter and how do you create a custom pattern?
DateTimeFormatter formats and parses date-time objects. Use `DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")` (or your pattern string). Letters like y=year, M=month, d=day, H=hour, m=minute, s=second.

### Q: How do you format a LocalDateTime (or LocalDate/LocalTime) with a DateTimeFormatter?
Use `dateTime.format(formatter)` or `formatter.format(dateTime)`. Both return a String. Example: `myDateTime.format(myFormatter)`.

### Q: What are predefined formatters in DateTimeFormatter?
Constants such as `DateTimeFormatter.ISO_LOCAL_DATE`, `DateTimeFormatter.ISO_LOCAL_TIME`, and `DateTimeFormatter.ISO_LOCAL_DATE_TIME`. Use the one that matches the type you are formatting (date, time, or date-time) to avoid runtime errors.

### Q: Does DateTimeFormatter replace SimpleDateFormat?
Yes. For java.time types (LocalDate, LocalTime, LocalDateTime), use DateTimeFormatter. SimpleDateFormat is for the legacy Date class and is not thread-safe; DateTimeFormatter is immutable and thread-safe.

### Q: How do you use a localized style with DateTimeFormatter?
Use `DateTimeFormatter.ofLocalizedDateTime(FormatStyle.MEDIUM)` (or FULL, LONG, SHORT). For date-only use ofLocalizedDate; for time-only use ofLocalizedTime. Match the formatter to the type you format.

### Q: Why must the formatter type match the date-time type (date vs time vs date-time)?
Using a date formatter on a time-only value (or vice versa) causes a runtime exception. Use ISO_LOCAL_DATE for LocalDate, ISO_LOCAL_TIME for LocalTime, ISO_LOCAL_DATE_TIME for LocalDateTime.

### Q: Is LocalDateTime immutable and thread-safe?
Yes. LocalDateTime is immutable and thread-safe, like LocalDate and LocalTime. Methods such as plusHours or minusDays return a new instance.

### Q: How do you add or subtract time from a LocalDateTime?
Use plus/minus methods: `dateTime.plusHours(3)`, `dateTime.minusDays(2)`, `dateTime.plusMinutes(30)`, etc. They return a new LocalDateTime; the original is unchanged.
