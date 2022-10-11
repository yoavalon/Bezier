d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.position_pen(3,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(0,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.long)

d.end()
