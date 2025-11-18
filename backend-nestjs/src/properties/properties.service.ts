import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

@Injectable()
export class PropertiesService {
  async list() {
    return prisma.property.findMany({ take: 50 });
  }
  async create(dto: any) {
    return prisma.property.create({ data: dto });
  }
}
