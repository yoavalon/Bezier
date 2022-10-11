d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.position_pen(3,0)

d.end()
