d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)

d.end()
