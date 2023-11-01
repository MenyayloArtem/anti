<?php

namespace RexepType;

class RexepType2 extends RexepTypeAbstract
{
    private const PARSE = [
        '.*?UserName:\s+([^\r\n]+)',
        '.*?ComputerName:\s+([^\r\n]+)',
        '.*?Country:\s+([^\r\n]+)',
        '.*?Location:\s+([^\r\n]+)',
        '.*?Zip\scode:\s+([^\r\n]+)',
        '.*?TimeZone:\s+([^\r\n]+)',
        '.*?Current\slanguage:\s+([^\r\n]+)',
        '.*?ScreenSize:\s+([^\r\n]+)',
        '.*?Operation\sSystem:\s+([^\r\n]+)',
        '.*?RAM:\s+([^\r\nl]+)',
    ];

    /**
     * @var string[]
     */
    private const PARAMS = [
        'username',
        'computerName',
        'country',
        'location',
        'zipCode',
        'timeZone',
        'currentLanguage',
        'screenSize',
        'operationSystem',
        'ram',
    ];

    private function __construct(string $path)
    {
        $this->path = $path;
    }

    public static function parse(string $path)
    {
        $self = new self($path);
        return $self->generateParams(self::PARSE, self::PARAMS);
    }
}