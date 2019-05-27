/**
 * Imports
 */

// Packages
import gulp            from 'gulp'
import gulpLoadPlugins from 'gulp-load-plugins'
import browserSync     from 'browser-sync'
import babelify        from 'babelify'
import browserify      from 'browserify'
import source          from 'vinyl-source-stream'
import buffer          from 'vinyl-buffer'
import watchify        from 'watchify'

// Loader
const $ = gulpLoadPlugins()

// Session
browserSync.create()

/**
 * Definition
 */

// Messages
const message = {
  compiled   : '<%= file.relative %>: file compiled',
  transpiled : '<%= file.relative %>: file transpiled',
  updated    : '<%= file.relative %>: file updated',
  minified   : '<%= file.relative %>: file minified',
  cleaned    : '<%= file.relative %>: file cleaned',
  error      : '<%= error.message %>'
}

/**
 * Configuration
 */

// Server
gulp.task('server', ['styles', 'scripts'], () => {
  browserSync.init({
    proxy: 'http://localhost',
    browser: 'Google Chrome'
  })
  gulp.watch([
    `sources/styles/**/*.scss`,
    `sources/styles/*.scss`
  ], ['styles'])
})

// Styles
gulp.task('styles', () => {
  return gulp.src(`sources/styles/app.scss`)
    .pipe($.plumber())
    .pipe($.sourcemaps.init({ loadMaps: true }))
    .pipe($.sass())
    .on('error', $.notify.onError({
      title   : "Styles",
      message : message.error,
      sound   : "beep"
    }))
    .pipe($.autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false
    }))
    .pipe($.sourcemaps.write('./'))
    .pipe(gulp.dest(`static/styles/`))
    .pipe(browserSync.stream())
    .pipe($.notify({
      title   : "Styles",
      message : message.compiled,
      sound   : "beep"
    }))
})

// Scripts
let bundler = null

const bundle = () => {
  bundler.bundle()
    .pipe($.plumber())
    .on('error', $.notify.onError({
      title   : "Scripts",
      message : message.error,
      sound   : "beep"
    }))
    .pipe(source('app.js'))
    .pipe(buffer())
    .pipe($.sourcemaps.init({ loadMaps: true }))
    .pipe($.sourcemaps.write('./'))
    .pipe(gulp.dest(`static/scripts/`))
    .pipe(browserSync.stream())
    .pipe($.notify({
      title   : "Scripts",
      message : message.transpiled,
      sound   : "beep"
    }))
}

gulp.task('scripts', () => {
  bundler = browserify({
    entries : `sources/scripts/app.js`,
    debug   : true,
    paths   : ['./node_modules', `sources/scripts/`]
  })
  .transform(babelify)
  bundler.plugin(watchify)
  bundler.on('update', bundle)
  bundle()
})

// CSS
gulp.task('compile', () => {
  return gulp.src(`static/styles/app.css`)
    .pipe($.cssnano())
    .on('error', $.notify.onError({
      title   : "Styles",
      message : message.error,
      sound   : "beep"
    }))
    .pipe(gulp.dest(`static/styles/`))
    .pipe($.notify({
      title   : "Styles",
      message : message.minified,
      sound   : "beep"
    }))
})

// JS
gulp.task('transpile', () => {
  return gulp.src(`static/scripts/app.js`)
    .pipe($.uglify())
    .on('error', $.notify.onError({
      title   : "Scripts",
      message : message.error,
      sound   : "beep"
    }))
    .pipe(gulp.dest(`static/scripts/`))
    .pipe($.notify({
      title   : "Scripts",
      message : message.minified,
      sound   : "beep"
    }))
})

// Images
gulp.task('minify', () => {
  return gulp.src(`static/images/*.+(png|jpg|jpeg|gif|svg)`)
    .pipe($.imagemin())
    .on('error', $.notify.onError({
      title   : "Images",
      message : message.error,
      sound   : "beep"
    }))
    .pipe(gulp.dest(`static/images/`))
    .pipe($.notify({
      title   : "Images",
      message : message.minified,
      sound   : "beep"
    }))
})

// Maps
gulp.task('clear', () => {
  return gulp.src([
    `static/scripts/app.js.map`,
    `static/styles/app.css.map`
  ])
    .pipe($.clean({
      force: true,
      read: false
    }))
    .on('error', $.notify.onError({
      title   : "Maps",
      message : message.error,
      sound   : "beep"
    }))
    .pipe($.notify({
      title   : "Maps",
      message : message.cleaned,
      sound   : "beep"
    }))
})

// Production
gulp.task('prod', ['compile', 'transpile', 'minify', 'clear'])

// Run
gulp.task('default', ['server'])
