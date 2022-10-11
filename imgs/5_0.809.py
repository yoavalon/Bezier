d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)

d.end()
