<?php

namespace RexepType;

class RexepType1 extends RexepTypeAbstract
{
    private const PARSE = [
        '.*?UserName:\s+([^\r\n]+)',
        '.*?Country:\s+([^\r\n]+)',
        '.*?Zip\sCode:\s+([^\r\n]+)',
        '.*?[^\w]Location:\s+([^\r\n]+)',
        '.*?Current\sLanguage:\s+([^\r\n]+)',
        '.*?ScreenSize:\s+([^\r\n]+)',
        '.*?TimeZone:\s+([^\r\n]+)',
        '.*?Operation\sSystem:\s+([^\r\n]+)',
        '.*?Total\sof\sRAM.*?(\d+)(?=\sbytes)',
        '.*?(\d+)(?=\sCores)',
    ];

    /**
     * @var string[]
     */
    private const PARAMS = [
        'username',
        'country',
        'zipCode',
        'location',
        'currentLanguage',
        'screenSize',
        'timeZone',
        'operationSystem',
        'ram',
        'cores',
    ];

    public static function parse(string $path)
    {
        $self = new self($path);
        return $self->generateParams(self::PARSE, self::PARAMS);
    }
}