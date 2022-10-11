d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.E, Length.long)
d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.position_pen(2,1)

d.end()
