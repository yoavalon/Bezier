d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)

d.end()
