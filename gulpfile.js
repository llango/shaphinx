// 用于构建css和javascript。

var gulp = require('gulp')
var concat = require('gulp-concat')
var postcss = require('gulp-postcss')
var rename = require('gulp-rename')
var sass = require('gulp-sass')
var sourcemaps = require('gulp-sourcemaps')
var uglify = require('gulp-uglify')

var Fiber = require('fibers')
sass.compiler = require('sass')

var autoprefixer = require('autoprefixer')
var cssnano = require('cssnano')
var easyImport = require('postcss-easy-import')

var plugins = [easyImport(), autoprefixer(), cssnano()]
var srcPath = './shaphinx/assets/'
var destPath = './shaphinx/theme/shaphinx/static'

function css () {
  return gulp
    .src(srcPath + 'styles/[!_]*.sass', { since: gulp.lastRun(css) })
    .pipe(sourcemaps.init())
    .pipe(sass({ fiber: Fiber }).on('error', sass.logError))
    .pipe(postcss(plugins))
    .pipe(rename({ dirname: 'styles', extname: '.css' }))
    .pipe(sourcemaps.write(''))
    .pipe(gulp.dest(destPath))
}

function javascript (cb) {
  return gulp
    .src(srcPath + 'scripts/[!_]*.js', { since: gulp.lastRun(javascript) })
    .pipe(sourcemaps.init())
    .pipe(concat('scripts/main.js'))
    .pipe(uglify())
    .pipe(sourcemaps.write(''))
    .pipe(gulp.dest(destPath))
}

exports.build = gulp.parallel(javascript, css)
