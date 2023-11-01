<?php

use RexepType\RexepType1;
use RexepType\RexepType2;
use RexepType\RexepType3;

require 'Php/vendor/autoload.php';

const TYPE_1 = 'UserInformation.txt';
const TYPE_2 = 'SystemInformation.txt';
const TYPE_3 = 'System.txt';

/**
 * @var Callable[]
 */
$parsers = [
    TYPE_1 => fn($folder) => RexepType1::parse($folder . '/' . TYPE_1),
    TYPE_2 => fn($folder) => RexepType2::parse($folder . '/' . TYPE_2),
    TYPE_3 => fn($folder) => RexepType3::parse($folder . '/' . TYPE_3),
];

[$command, $folder, $file] = $_SERVER['argv'];

echo json_encode($parsers[$file]($folder));