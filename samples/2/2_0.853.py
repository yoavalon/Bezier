d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)

d.end()
