d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)

d.end()
