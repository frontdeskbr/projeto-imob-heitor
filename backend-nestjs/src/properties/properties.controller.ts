import { Controller, Get, Post, Body } from '@nestjs/common';
import { PropertiesService } from './properties.service';

@Controller('api/properties')
export class PropertiesController {
  constructor(private readonly service: PropertiesService) {}

  @Get()
  list() {
    return this.service.list();
  }

  @Post()
  create(@Body() dto: any) {
    return this.service.create(dto);
  }
}
