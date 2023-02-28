""" """
from __future__ import unicode_literals, division, print_function, absolute_import

import argparse
import importlib
import os
import sys

import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

from vendor.sqlalchemy_codegen.codegen import modelcodegen
from vendor.sqlalchemy_codegen.codegen.controllercodegen.codegenerator import CodeGenerator as ControllerCodeGenerator
from vendor.sqlalchemy_codegen.codegen.modelcodegen.codegen import CodeGenerator as SQLCodeGenerator
from vendor.sqlalchemy_codegen.codegen.utils.tablesMetadata import TableMetadata


def import_dialect_specificities(engine):
    dialect_name = '.' + engine.dialect.name
    try:
        importlib.import_module(dialect_name, 'modelcodegen.dialects')
    except ImportError:
        pass


def main():
    parser = argparse.ArgumentParser(description='Generates SQLAlchemy model code from an existing database.')
    parser.add_argument('url', nargs='?', help='SQLAlchemy url to the database')
    parser.add_argument('--version', action='store_true', help="print the version number and exit")
    parser.add_argument('--schema', help='load tables from an alternate schema')
    parser.add_argument('--tables', help='tables to process (comma-separated, default: all)')
    parser.add_argument('--noviews', action='store_true', help="ignore views")
    parser.add_argument('--noindexes', action='store_true', help='ignore indexes')
    parser.add_argument('--noconstraints', action='store_true', help='ignore constraints')
    parser.add_argument('--nojoined', action='store_true', help="don't autodetect joined table inheritance")
    parser.add_argument('--noinflect', action='store_true', help="don't try to convert tables names to singular form")
    parser.add_argument('--noclasses', action='store_true', help="don't generate classes, only tables")
    parser.add_argument('--notables', action='store_true', help="don't generate tables, only classes")
    parser.add_argument('--outdir', help='file to write output to (default: stdout)')
    parser.add_argument('--models_layer', action='store_true', help='model file to write output to direction models')
    parser.add_argument('--controller_layer', action='store_true',
                        help='controller file to write output to direction controllers')
    parser.add_argument('--nobackrefs', action='store_true', help="don't include backrefs")
    parser.add_argument('--flask', action='store_true', help="use Flask-SQLAlchemy columns")
    parser.add_argument('--ignore-cols',
                        help="Don't check foreign key constraints on specified columns (comma-separated)")
    parser.add_argument('--nocomments', action='store_true', help="don't render column comments")
    args = parser.parse_args()

    if args.version:
        print(modelcodegen.version)
        return
    if not args.url:
        print('You must supply a url\n', file=sys.stderr)
        parser.print_help()
        return
    engine = create_engine(args.url)
    import_dialect_specificities(engine)
    metadata = MetaData(engine)

    # from sqlalchemy.engine import reflection
    # bind = reflection.Inspector(inflect_engine)
    # views = bind.get_view_names()

    tables = args.tables.split(',') if args.tables else None
    ignore_cols = args.ignore_cols.split(',') if args.ignore_cols else None
    metadata.reflect(engine, args.schema, not args.noviews, tables)
    outdir = args.outdir if args.outdir else sys.stdout
    generator = SQLCodeGenerator(metadata, args.noindexes, args.noconstraints,
                                 args.nojoined, args.noinflect, args.nobackrefs,
                                 args.flask, ignore_cols, args.noclasses, args.nocomments, args.notables)

    if args.models_layer:
        model_dir = os.path.join(outdir, 'models')
        os.makedirs(model_dir, exist_ok=True)
        generator.render(model_dir)

    if args.controller_layer:
        controller_dir = os.path.join(outdir, 'controller')
        os.makedirs(controller_dir, exist_ok=True)
        reflection_views = [model.table.name for model in generator.models if type(model) == modelcodegen.codegen.ModelTable]
        views = sqlalchemy.inspect(engine).get_view_names()
        for table_name in set(reflection_views) ^ set(views):
            print(f"\033[33mWarnning: Table {table_name} required PrimaryKey!\033[0m")
        table_dict = TableMetadata.get_tables_metadata(
            metadata=metadata,
            reflection_views=reflection_views,
        )
        generator = ControllerCodeGenerator(table_dict, args.flask, args.url)
        generator.controller_codegen(controller_dir=controller_dir)


# 开始生成代码，通过函数调用方式
def start_generate(**kwargs):

    if kwargs.get('version'):
        print(modelcodegen.version)
        return
    if not kwargs.get('url'):
        print('You must supply a url\n', file=sys.stderr)
        # parser.print_help()
        return
    engine = create_engine(kwargs.get('url'))
    import_dialect_specificities(engine)
    metadata = MetaData(engine)

    # from sqlalchemy.engine import reflection
    # bind = reflection.Inspector(inflect_engine)
    # views = bind.get_view_names()

    tables = kwargs.get('table').split(',') if kwargs.get('table') else None
    ignore_cols = kwargs.get('ignore_cols').split(',') if kwargs.get('ignore_cols') else None
    metadata.reflect(engine, kwargs.get('schema'), not kwargs.get('noviews'), tables)
    outdir = kwargs.get('outdir') if kwargs.get('outdir') else sys.stdout
    generator = SQLCodeGenerator(metadata, kwargs.get('noindexesr'), kwargs.get('noconstraints'),
                                 kwargs.get('nojoined'), kwargs.get('noinflect'), kwargs.get('nobackrefs'),
                                 kwargs.get('flask'), ignore_cols, kwargs.get('noclasses'), kwargs.get('nocomments'), kwargs.get('notables'))

    if kwargs.get('models_layer'):
        model_dir = os.path.join(outdir, 'models')
        os.makedirs(model_dir, exist_ok=True)
        generator.render(model_dir)

    if kwargs.get('controller_layer'):
        controller_dir = os.path.join(outdir, 'controller')
        os.makedirs(controller_dir, exist_ok=True)
        reflection_views = [model.table.name for model in generator.models if
                            type(model) == modelcodegen.codegen.ModelTable]
        views = sqlalchemy.inspect(engine).get_view_names()
        for table_name in set(reflection_views) ^ set(views):
            print(f"\033[33mWarnning: Table {table_name} required PrimaryKey!\033[0m")
        table_dict = TableMetadata.get_tables_metadata(
            metadata=metadata,
            reflection_views=reflection_views,
        )
        generator = ControllerCodeGenerator(table_dict, kwargs.get('flask'), kwargs.get('url'))
        generator.controller_codegen(controller_dir=controller_dir)


if __name__ == '__main__':

    # test
    kwargs = {
        "url": 'mysql+pymysql://dev_python_online_exam:dev_python_online_exam@47.94.236.132:13306/python_online_exam?charset=utf8',
        "tables": 'course,knowledge,sys_class,paper_topic,student_course,sys_college,exam,student_exam_result,sys_school,topic_choice_single,paper,student,exam_paper,paper_part,teacher,discipline,topic_programme,topic_judge,user_student,topic_choice_multiple,topic_blank,user_teacher,v_paper_manage,v_exam_manage,v_course_manage,v_student_manage,v_student_exam_result',
        'models_layer': 'yes',
        "outdir": 'D:/dist/te\z1101011',
        'flask': 'yes'
    }
    start_generate(**kwargs)