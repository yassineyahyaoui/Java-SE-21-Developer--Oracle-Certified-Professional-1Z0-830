# Day 38 -- Advanced Topics + Modules/Packaging

### Q: How do you handle exceptions that escape from a thread so the main thread is aware?
Use `Thread.setUncaughtExceptionHandler(UncaughtExceptionHandler)`. The handler’s `uncaughtException(Thread t, Throwable e)` is invoked when that thread terminates due to an uncaught exception. Set it per thread or via `Thread.setDefaultUncaughtExceptionHandler` for all threads.

### Q: How does ReentrantLock differ from synchronized?
ReentrantLock allows explicit `lock()`/`unlock()` (or try-with-resources via `lock()` returning a condition), supports fairness (FIFO acquisition), `tryLock()` for non-blocking acquire, and interruptible wait. synchronized is built-in and simpler but does not offer these options.

### Q: When is ReadWriteLock preferred over a single exclusive lock?
When reads are much more frequent than writes. ReadWriteLock allows multiple threads to hold the read lock concurrently but only one thread the write lock. This improves throughput in read-heavy scenarios compared to a single exclusive lock.

### Q: What is StampedLock’s optimistic read and how do you use it?
Optimistic read is a non-blocking read that does not block writers. Call `tryOptimisticRead()` to get a stamp, read the data, then call `validate(stamp)` to ensure no write occurred; if invalid, acquire a full read lock and retry. Suited for read-heavy, low-contention cases.

### Q: How do you release a StampedLock and why is it different from ReentrantLock?
StampedLock does not implement `Lock`, so there is no try-with-resources. You must call `unlockRead(stamp)`, `unlockWrite(stamp)`, or `unlock(stamp)` with the stamp returned when acquiring the lock. Forgetting to unlock or validate can cause deadlock or inconsistent data.

### Q: How would you build a multithreaded web server that handles each request concurrently?
Use a `ServerSocket` that accepts connections on a port. For each accepted `Socket`, either create a new thread (thread-per-request) or submit a `Runnable` (e.g. a `ClientHandler`) to an `ExecutorService` (thread pool). The handler reads the request from the socket’s input stream and writes the HTTP response to the output stream.

### Q: What does module-info.java require and exports do?
`requires` declares a dependency on another module (e.g. `requires java.sql;`). `exports` makes a package visible to other modules (e.g. `exports com.app.api;`). Only exported packages are accessible to other modules.

### Q: What is requires transitive and when is it used?
`requires transitive M;` means this module requires M and any module that requires the current module also reads M. It is used when the module’s public API uses types from M so callers need that dependency too.

### Q: What do opens and provides/uses do in module-info.java?
`opens` opens a package for reflection (e.g. for frameworks). `provides X with Y` declares a service implementation: this module provides implementation Y for service interface X. `uses X` declares that the module uses the service X (and can load it via `ServiceLoader`).

### Q: What is an automatic module and how is it created?
An automatic module is a non-modular JAR placed on the module path. The module name is derived from the JAR filename (or `Automatic-Module-Name` in the manifest). It reads all other modules and exports all its packages, bridging the class path and the module system.

### Q: How do you compile multiple modules from source with javac?
Use `javac --module-source-path <path> -d <out> -m <module1>,<module2>,...` so that `<path>` contains module directories (each with its `module-info.java` and package tree). Alternatively compile per module with `-p`/`--module-path` for dependencies.

### Q: How do you run a modular application with java?
Use `java --module-path <path> (-p <path>) -m <module>/<main-class>` to put module artifacts on the module path and start the main class in the given module. The main class can be set in module-info with `opens` or in the JAR manifest.

### Q: What are jdeps and jlink used for?
`jdeps` analyzes dependencies of classes or JARs (e.g. `jdeps --module-path <path> <jar>`), useful for seeing module dependencies. `jlink` builds a custom runtime image containing only the modules you need: `jlink -p <path> --add-modules <modules> --output <dir>`.

### Q: How do you create a JAR that can be used on the module path?
Put `module-info.class` in the JAR (compile with `javac`). The JAR is then a modular JAR. For an executable JAR with a main class, either specify the main class in the module (`module-info.java`) or in the JAR manifest (`Main-Class` and optionally `Main-module` for `-m`).
