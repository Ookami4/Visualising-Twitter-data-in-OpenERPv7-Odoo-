from openerp.osv import osv,fields
import openerp

class model_johnson(osv.osv):
    _name="twitter.johnson"
    _columns={
        'tweet':fields.char("Tweet",required=True),
        'polarite':fields.float("Polarite",required=True)
    }
    def create(self, cr, uid, values, context=None):
        out=super(model_johnson, self).create(cr, uid, values, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.johnstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        return out
    def write(self, cr, uid,ids, values, context=None):
        out=super(model_johnson, self).write(cr, uid,ids, values, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.johnstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        return out
    def unlink(self, cr, uid, values, context=None):
        out=super(model_johnson, self).unlink(cr, uid, values, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.johnstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        return out
model_johnson()