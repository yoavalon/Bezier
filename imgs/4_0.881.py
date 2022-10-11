d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)

d.end()
