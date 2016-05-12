'use strict';

// Require packages

var gulp = require('gulp'),
	gutil = require('gulp-util'),
	sass = require('gulp-sass'),
	sourcemaps = require('gulp-sourcemaps'),
	concat = require('gulp-concat'),
	autoprefixer = require('gulp-autoprefixer'),
	cleanCSS = require('gulp-clean-css'),
	uglify = require('gulp-uglify');

// Define our paths

var SASS_PATH = './scss/',
	CSS_PATH = './css/',
	SASS_FILE = 'main.scss',
	CSS_FILE = 'main.min.css',
	JS_PATH = './js/',
	JS_FILE = 'main.js',
	JS_MIN_FILE = 'main.min.js';


// Define default options

var cleanCSSOpts = {
	recursivelyOptimizeBlocks: true,
	removeDuplicates: true,
	restructure: true,
	keepSpecialComments: 0,
	compatibility: 'ie8',
};

var SASSOpts = {
	outputStyle: 'compressed',
	sourceComments: false,
};

var autoprefixerOpts = {
	browsers: ['> 0.1%', 'IE 8', 'iOS 6', 'Android 4'],
	cascade: false,
};

// `gulp sass`
gulp.task('sass', function() {
	return gulp.src(SASS_PATH + SASS_FILE)
		.pipe(sourcemaps.init())
		.pipe(sass(SASSOpts)
		.on('error', sass.logError))
		.pipe(autoprefixer(autoprefixerOpts))
		.pipe(cleanCSS(cleanCSSOpts))
		.pipe(concat(CSS_FILE))
		.pipe(sourcemaps.write('./'))
		.pipe(gulp.dest(CSS_PATH));
});

// `gulp sass:watch`
gulp.task('sass:watch', function() {
	gulp.watch(SASS_PATH + '**/*.scss', ['sass']);
});


// `gulp js`
gulp.task('js', function() {
	return gulp.src(JS_PATH + JS_FILE)
		.pipe(sourcemaps.init())
		.pipe(uglify())
		.pipe(concat(JS_MIN_FILE))
		.pipe(sourcemaps.write('./'))
		.pipe(gulp.dest(JS_PATH));
});

// `gulp js:watch`
gulp.task('js:watch', function() {
	gulp.watch(JS_PATH + '**/*.js', ['js']);
});


// `gulp` default command

gulp.task('default', ['sass', 'js']);
